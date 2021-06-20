<template>
  <div style="text-align: center">
    <h1>Lose..</h1>
    <img class="loser" src="@/assets/AI.png" alt="">
    <br>
    <h4>AI가 세상을 지배한다 깔깔</h4>
  </div>
</template>

<script>
export default {
  name: 'Lose'
}
</script>

<style scoped>
.loser {
  animation-iteration-count: infinite;
  animation-duration: 2s;
  animation-name: rotate;
}

@keyframes rotate {
  from {
    transform: rotateY( 0deg );
  }

  to {
    transform: rotateY( 180deg );
  }
}

</style>