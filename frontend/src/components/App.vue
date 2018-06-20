<template>
  <div>
    <div style="display: flex;">
      <Maps style="flex: 1;" />
      <TrekksFilter style="flex: 1;" />
    </div>

    <Umbler />

  </div>
</template>

<script lang="ts">
    import Maps from '@components/Maps'
    import TrekksFilter from '@components/TrekksFilter'
    import Umbler from '@components/Umbler.vue'
    import Vue from 'vue'
    export default Vue.extend({
    components: {
      Maps,
      TrekksFilter,
      Umbler,
    },
    name: 'App',
  })
</script>

<style>
</style>