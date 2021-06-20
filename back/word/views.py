from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Word
import requests
from bs4 import BeautifulSoup
import random

import os
BASE_URL = os.environ['WORD_API_URL']



@api_view(['POST'])
def user_input(request, foreign, txtlen): # 사용자의 입력이 올바른지 확인
  user_input = request.data['content'] # 사용자 입력
  # 옵션 정보
  if foreign :
      lan = 'native,chinese,loanword'
  else:
      lan = 'native,chinese'

  # 1. 중복되는 단어가 있는지
  if Word.objects.filter(word=user_input).exists():
    return Response({'result': 2, 'msg': '중복단어가 있습니다.'})

  # 2. 끝말잇기 규칙에 맞는지  
  if Word.objects.exists(): # DB에 단어가 한개 이상 존재하는 경우
    last_word = Word.objects.order_by('-pk')[0].word[-1]
    if not ((last_word == user_input[0]) or ('라' <= last_word <= '맇' and ord(user_input[0])-ord(last_word) == 3528 ) or ('나' <= last_word <= '닣' and ord(user_input[0])-ord(last_word) == 5292 )):
      return Response({'result': 3, 'msg': '끝말잇기 규칙에 맞지 않습니다.'})

  # 3. 존재하는 단어인지
  isExists = f'{BASE_URL}&q={user_input}&advanced=y&target=1&method=exact&pos=1&letter_s={int(txtlen)}&type2={lan}'
  response = requests.get(isExists)
  soup = BeautifulSoup(response.text, 'html.parser')
  flag = int(soup.find('total').string)
  if not flag:
    return Response({'result': 4, 'msg': '존재하지 않는 단어입니다.'})

  # 4. DB 저장
  Word.objects.create(word=user_input)
  return Response({'result': 1, 'msg': '통과'})


@api_view(['POST'])
def ai_input(request, foreign, txtlen):
  last_word = Word.objects.order_by('-pk')[0].word[-1] # 마지막 단어의 마지막 말

  # 옵션 정보
  if foreign :
      lan = 'native,chinese,loanword'
  else:
      lan = 'native,chinese'

  # last_word으로 시작하는 명사가 몇개인지 확인
  total_url = f'{BASE_URL}&q={last_word}&start=1&num=10&advanced=y&target=1&method=start&pos=1&letter_s={int(txtlen)}&type2={lan}'
  response = requests.get(total_url)
  soup = BeautifulSoup(response.text, 'html.parser')
  total = int(soup.find('total').string)

  # 전체 페이지이지에서 랜덤으로 한개의 페이지 선택
  if total > 10:
    page = random.choice(range(1, total // 10 + 1))
  elif total > 0:
    page = 1
  else:
      # 두음법칙
      if '라' <= last_word <= '맇':
        last_word2 = chr(ord(last_word) + 3528)
      elif '나' <= last_word <= '닣':
        last_word2 = chr(ord(last_word) + 5292)
      else:
        return Response({'result': 5, 'msg': '당신이 이겼습니다'})
    
      # 녕,냥,량,령 원글자가 이런 없는 단어인 경우 두음법칙 적용
      total_url = f'{BASE_URL}&q={last_word2}&start=1&num=10&advanced=y&target=1&method=start&pos=1&letter_s={int(txtlen)}&type2={lan}'
      response = requests.get(total_url)
      soup = BeautifulSoup(response.text, 'html.parser')
      total = int(soup.find('total').string)

      if total > 10:
        page = random.choice(range(1, total // 10 + 1))
      elif total > 0:
        page = 1
      else:
        # 두음법칙으로 자음을 'ㅇ'으로 바꿨는데도 안되면 진짜 이긴거
        return Response({'result': 5, 'msg': '당신이 이겼습니다'})

      last_word = last_word2

  # 해당 url에서 결과 단어 리스트 추출
  url = f'{BASE_URL}&q={last_word}&start={page}&num=10&advanced=y&target=1&method=start&pos=1&letter_s={int(txtlen)}&type2={lan}'
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  words = list(soup.find_all('word'))

  # 한개만 뽑아서 전처리
  word = random.choice(words)
  tell_word = word.string.replace('-','')

  # 뽑은 단어 DB에 저장
  Word.objects.create(word=tell_word)

  return Response({'result': 1, 'msg': '통과', 'word': tell_word})


@api_view(['POST'])
def reset(request):
  Word.objects.all().delete()
  return Response({'msg': '게임 시작'})