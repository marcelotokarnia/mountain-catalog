<template>
  <div class="container main">
    <slot></slot>
  </div>
</template>

<script lang="ts">
  import Vue from 'vue'
  export default Vue.extend({
    name: 'Main',
  })
</script>

<style scoped lang="stylus">
  .main
    max-width 95vw !important
    height 95vh
    padding-top 4rem
    padding-bottom 3rem
</style>