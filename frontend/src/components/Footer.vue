<template>
  <nav class="navbar navbar-expand-md navbar-success bg-success fixed-bottom">
    <Umbler />
  </nav>
</template>

<script lang="ts">
    import Umbler from '@components/Umbler.vue'
    import Vue from 'vue'
    export default Vue.extend({
    components: {
      Umbler,
    },
    name: 'Footer',
  })
</script>

<style scoped lang="stylus">
  .navbar
    height 3.5rem
</style>