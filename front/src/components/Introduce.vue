<template>
  <div>
    <div>
      <h3 class="subHeadline">쿵쿵따</h3>
      <div>
        <div>1. 입력하는 단어가 국립국어원 사전에 등재된 단어여야 합니다.</div>
        <div>2. 한방 단어 사용이 가능합니다</div>
        <div>3. 두음 법칙이 적용됩니다. (ex. 림 -> 임) </div>
        <div>4. 중복 단어 사용 불가 </div>
      </div>
      <br>
      <br>
      <div class="Button" @click="Next">Next</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Introduce',
  methods: {
    Next() {
      this.$emit('status-change', 2)
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


.Button {
  color: white;
  font-size: 30px;
  background-color: rgb(81, 112, 24);
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
  background-color: rgb(101, 139, 30);
  box-shadow: 1px 5px 0px rgba(0, 0, 0, 0.119);
}
</style>