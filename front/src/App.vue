<template>
  <div id="app">
    <div class="stage-area shadow-lg">
      <div class="logoTop">JSJS</div>
      <div class="topLine"></div>
      <div class="screenArea">
        <div class="d-flex justify-content-center align-items-center">
          <div>
            <div class="purpleLine" style="width: 260px"></div>
            <div class="darkBuleLine" style="width: 260px"></div>
          </div>
          <div>Created by js jy</div>
          <div>
            <div class="purpleLine" style="width: 170px"></div>
            <div class="darkBuleLine" style="width: 170px"></div>
          </div>
        </div>
        <div class="d-flex align-items-center">
          <div class="ms-2">
            <div class="redCircle"></div>
            <div><small>BATTERY</small></div>
          </div>
          <div class="realScreenArea">
            <Introduce v-if="status === 1" @status-change="StatusChange"/>
            <SelectOptions v-else-if="status === 2" @status-change="StatusChange" @set-game-options="setGameOption"/>
            <GameStage v-else-if="status === 3"
              :foreign="foreign"
              :textLen="textLen"
              @status-change="StatusChange"
              />
            <Lose v-else-if="status === 4"/>
            <Win v-else-if="status === 5"/>
          </div>
        </div>
      </div>


      <div>
        <h3 class="ms-3" style="color: #4d558c">JSJS GAME PLAYER</h3>
        <img class="bottomBtns" src="@/assets/buttons.png" alt="">
      </div>
    </div>
  </div>
</template>

<script>
import Introduce from './components/Introduce.vue'
import SelectOptions from './components/SelectOptions.vue'
import GameStage from './components/GameStage.vue'
import Lose from './components/Lose.vue'
import Win from './components/Win.vue'

export default {
  name: 'App',
  data() {
    return {
      status: 1,
      foreign: 1,
      textLen: 2,
    }
  },
  components: {
    Introduce,
    SelectOptions,
    GameStage,
    Lose,
    Win,
  },
  methods: {
    StatusChange(value) {
      this.status = value
    },
    setGameOption(foreign, textLen) {
      this.foreign = foreign
      this.textLen = textLen
    }
  }
}
</script>

<style>
#app {
  font-family: 둥근모꼴, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #ffffff;
  margin-top: 30px;
}

.stage-area {
  margin: auto;
  border: solid 2px #202020;
  border-radius: 10px 10px 100px 10px;
  width: 650px;
  height: 850px;
  background-color: #dedce0;
}

.logoTop {
  color: #9b9898;
  text-align: center;
  border: solid 1px #9b9898;
  border-radius: 20px;
  font-size: 12px;
  margin: 10px 10px;
  width: 50px
}

.topLine {
  color: #7a797f;
  background-color: #7a797f;
  height: 2px;
  margin-bottom: 20px;
}

.screenArea {
  width: 610px;
  height: 480px;
  margin: 0px auto;
  background-color: #5d6a7a;
  border-radius: 2% 2% 15% 2%;
  border: solid 2px #2b2b2b;
}

.realScreenArea {
  width: 480px;
  height: 400px;
  margin: 10px 20px;
  padding: 25px;
  background-color: #78b53c;
  border: solid 2px #2b2b2b;
  box-shadow: inset 7px 7px rgba(0, 0, 0, .24);
}

.purpleLine {
  background-color: #5b526e;
  height: 4px;
  margin: 2px 10px;
}

.darkBuleLine {
  background-color: #3d4961;
  height: 4px;
  margin: 2px 10px;
}

.redCircle {
  margin-top: 3px;
  margin-right: 3px;
  margin-left: 16px;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background-color: rgb(199, 14, 14);
  border: solid 2px #0f0f0f;
  transition-duration: 0.5s;
}

.redCircle:hover {
  background-color: rgb(255, 65, 65);
}

.bottomBtns {
  margin-top: 10px;
  margin-left: 40px;
  height: 250px;
}
</style>
