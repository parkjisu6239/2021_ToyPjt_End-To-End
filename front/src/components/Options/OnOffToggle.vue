<template>
  <div style="height: 2rem; position: relative;">
    <div :class="{ optionBody: true, optionBodyTrue: option, optionBodyFalse: !option}" @click="toggleOption">
      <div class="optionText">
        <p v-if="option">On</p>
        <p v-else>Off</p>
      </div>
      <div :class="{ optionCircle: true, optionCircleTrue: option, optionCircleFalse: !option}"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'OnOffToggle',
  data() {
    return {
      option: 1,
    }
  },
  methods: {
    toggleOption() {
      this.option = (this.option + 1) % 2
      this.$emit('foreign-option', this.option)
    }
  }
}
</script>

<style>
.optionBody{
  width: 5.5rem;
  height: 2rem;
  border-radius: 15px;
  z-index: 0;
  position: absolute;
  cursor: pointer;
  transition-duration: 0.5s;
}

.optionBodyTrue{
  background-color: #FFC107;
}

.optionBodyFalse{
  background-color: #bebebe;
}

.optionText{
  padding-top: 4px;
  padding-left: 34px;
  z-index: 1;
  position: absolute;
}

.optionCircle {
  margin-top: 3px;
  margin-right: 3px;
  margin-left: 3px;
  width: 1.5rem;
  height: 1.5rem;
  border-radius: 50%;
  background-color: white;
  z-index: 2;
  position: relative;
  transition-duration: 0.5s;
}

.optionCircleTrue {
  transform: translate(57px, 0px)
}

.optionCircleFalse {
  transform: translate(1px, 0px)
}
</style>