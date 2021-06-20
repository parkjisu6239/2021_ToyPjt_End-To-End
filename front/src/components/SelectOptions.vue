<template>
  <div>
    <h3 class="subHeadline">쿵쿵따</h3>
    <div style="color: rgb(81, 112, 24)">
      외래어 옵션을 설정하면 외래어 플레이어와 상대방 모두 외래어 사용이 가능합니다.
      플레이어가 입력한 단어의 길이가 최소 글자수 이상이어야 합니다.
    </div>
    <br>
    <div class="options">
      <p class="mt-1">외래어 허용 : </p>
      <OnOffToggle @foreign-option="foreignOption"/>
    </div>
    <div class="options">
      <p>최소 글자수 : </p>
      <SelectTextLen @textlen-option="textlenOption"/>
    </div>
    <div class="Button" @click="Start">Game Start!</div>
  </div>
</template>

<script>
import OnOffToggle from '@/components/Options/OnOffToggle'
import SelectTextLen from '@/components/Options/SelectTextLen'

import axios from 'axios'

export default {
  name: 'SelectOptions',
  data() {
    return {
      foreign: 1,
      textLen: 2,
    }
  },
  components: {
    OnOffToggle,
    SelectTextLen
  },
  methods: {
    Start() {
      this.$emit('status-change', 3)
      this.$emit('set-game-options', this.foreign, this.textLen)
      this.StartAxios()
    },
    foreignOption(value) {
      this.foreign = value
    },
    textlenOption(value){
      this.textLen = value
    },
    StartAxios() {
      axios.post(`${process.env.VUE_APP_API_URL}word/reset/`)
        .then(res => {
          console.log(res.data.msg)
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style scoped>

.subHeadline {
  margin: 0px auto;
  padding-top: 4px;
  margin-bottom: 2rem;
  text-align: center;
  background-color: rgb(81, 112, 24);
  border-radius: 20px;
  width: 150px;
  height: 40px;
}

.options {
  display: flex;
  margin: 0px auto;
}

.options p {
  margin-right: 1rem;
}

.Button {
  color: white;
  font-size: 30px;
  background-color: #8d185c;
  border-radius: 10px;
  text-align: center;
  width: 300px;
  height: 60px;
  padding-top: 5px;
  margin: 0px auto;
  transform: translate(0px, 20px);
  transition-duration: 0.1s;
  cursor: pointer;
}

.Button:hover {
  background-color: #af1d72;
  box-shadow: 1px 5px 0px rgba(0, 0, 0, 0.119);
}
</style>