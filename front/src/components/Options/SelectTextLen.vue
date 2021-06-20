<template>
  <div>
    <div class="checkBox">
      <div>
        <label for="2">2글자</label>
        <input id="2" name="textLen" v-model="selectedValue" value="2" type="radio">
      </div>
      <div>
        <label for="3">3글자</label>
        <input id="3" name="textLen" v-model="selectedValue" value="3" type="radio">
      </div>
      <div>
        <label for="4">4글자</label>
        <input id="4" name="textLen" v-model="selectedValue" value="4" type="radio">
      </div>
      <div>
        <label for="5">5글자</label>
        <input id="5" name="textLen" v-model="selectedValue" value="5" type="radio">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SelectTextLen',
  data(){
    return {
      selectedValue: 2
    }
  },
  watch: {
    selectedValue() {
      this.$emit('textlen-option', this.selectedValue*1)
    }
  }
}
</script>

<style>
.checkBox {
  display: flex;
}

.checkBox div {
  margin-right: 1rem;
}

.checkBox label {
  margin-right: 0.2rem;
}
</style>