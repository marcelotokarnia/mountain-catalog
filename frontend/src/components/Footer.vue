<template>
  <nav class="navbar navbar-expand-md navbar-success bg-success fixed-bottom">
    <Umbler />
  </nav>
</template>

<script lang="ts">
  import Vue from 'vue'
  import Umbler from '@components/Umbler.vue'
  export default Vue.extend({
    name: 'Footer',
    components: {
      Umbler
    }
  })
</script>

<style scoped lang="stylus">
  .navbar
    height 3.5rem
</style>