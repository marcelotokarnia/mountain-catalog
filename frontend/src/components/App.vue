<template>
  <div>
    <div style="display: flex;">
      <router-view style="flex: 1;"/>
      <TrekksFilter style="flex: 1;" />
    </div>

    <Umbler />
  </div>
</template>

<script lang="ts">
    import TrekksFilter from '@components/TrekksFilter'
    import Umbler from '@components/Umbler.vue'
    import Vue from 'vue'
    export default Vue.extend({
    components: {
      TrekksFilter,
      Umbler,
    },
    name: 'App',
  })
</script>

<style>
</style>