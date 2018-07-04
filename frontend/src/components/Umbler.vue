<template>
  <a href='https://app.umbler.com/u/yk4lz7pj'>
    <img
      src='https://static.umbler.com/brand/umbler-badges/umbler-badge-hostedby-light-bg.png'
      alt='Hosted by Umbler'
    />
  </a>
</template>

<script lang="ts">
  import Vue from 'vue'
  export default Vue.extend({
    name: 'Umbler',
  })
</script>

<style scoped lang="stylus">
  a
    line-height 3.5rem
    height 3.5rem
  a img
    height calc(100% - 1.5rem)
    margin auto
    vertical-align middle
    display inline-block
</style>