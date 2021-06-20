<template>
  <div>
    <h3 class="subHeadline">쿵쿵따</h3>
    <div class="d-flex justify-content-between">
      <div class="d-flex flex-column align-items-start">
        <span class="player-speech-bubble">{{ inputTxt }}</span>
        <div class="d-flex flex-column align-items-center">
          <img src="@/assets/player.png" alt="">
          <div>player</div>
        </div>
      </div>

      <div class="d-flex flex-column align-items-end justify-content-between">
        <span class="ai-speech-bubble"> {{ AItxt }} </span>
        <div class="d-flex flex-column align-items-center">
          <img src="@/assets/AI.png" alt="">
          <div>AI</div>
        </div>
      </div>
    </div>
    <br>
    <div class="input-group mb-3">
      <input @keyup.enter="UserInput" type="text" class="form-control" v-model="inputTxt" aria-describedby="button-addon" autofocus>
      <button @click="UserInput" class="btn btn-outline-success" type="button" id="button-addon">쿵쿵따!</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'GameStage',
  data() {
    return {
      inputTxt: '',
      AItxt: '...'
    }
  },
  props: {
    foreign: {
      type: Number
    },
    textLen: {
      type: Number
    }
  },
  methods: {
    UserInput(){
      axios.post(`${process.env.VUE_APP_API_URL}word/user/${this.foreign}/${this.textLen}/`, {content: this.inputTxt})
        .then(res => {
          // 통과
          if (res.data.result === 1) {
            this.AItxt = '...' // AI 생각중
            this.AIInput()// AI의 입력 요청 보내기
          } else { // Lose 화면 띄우기
            this.$emit('status-change', 4)
            console.log('당신이 졌습니다.', res.data.msg)
          }
        })
        .catch(err => {
          console.log(err)
        })

    },
    AIInput(){
      axios.post(`${process.env.VUE_APP_API_URL}word/ai/${this.foreign}/${this.textLen}/`)
        .then(res => {
          // 통과
          if (res.data.result === 1) {
            this.AItxt = res.data.word // AI 입력 말풍선에 업데이트
            this.inputTxt = '' // 인풋 비우기
          } else { // Win 화면 띄우기
            this.$emit('status-change', 5)
            console.log('당신이 이겼습니다.', res.data.msg)
          }
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

img {
  width: 150px;
  height: auto;
}


.ai-speech-bubble {
	position: relative;
	background: #5d6a7a;
  padding: 10px 20px;
	border-radius: .4em;
  text-align: end;
  min-width: 50px;
  min-height: 44px;
}

.ai-speech-bubble:after {
	content: '';
	position: absolute;
	bottom: 0;
	right: 20px;
	width: 0;
	height: 0;
	border: 15px solid transparent;
	border-top-color: #5d6a7a;
	border-bottom: 0;
	border-left: 0;
	margin-left: -7.5px;
	margin-bottom: -15px;
}

.player-speech-bubble {
	position: relative;
	background: rgb(81, 112, 24);
  padding: 10px 20px;
	border-radius: .4em;
  text-align: start;
  min-width: 50px;
  min-height: 44px;
}

.player-speech-bubble:after {
	content: '';
	position: absolute;
	bottom: 0;
	left: 20px;
	width: 0;
	height: 0;
	border: 15px solid transparent;
	border-top-color: rgb(81, 112, 24);
	border-bottom: 0;
	border-right: 0;
	margin-left: -7.5px;
	margin-bottom: -15px;
}

</style>