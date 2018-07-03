<template>
  <div class="main">
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
    display flex
    padding-top 4rem
</style>