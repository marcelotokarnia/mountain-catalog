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
    height 80vh
    max-width 95vw !important
    padding-top 4rem
</style>