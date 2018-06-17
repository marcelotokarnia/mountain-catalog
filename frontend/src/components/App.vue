<template>
  <div>
    <div style="display: flex;">
      <Maps style="flex: 1;" />
      <TracksFilter style="flex: 1;" />
    </div>

    <Umbler />

  </div>
</template>

<script lang="ts">
    import Maps from '@components/Maps.vue'
    import TracksFilter from '@components/TracksFilter'
    import Umbler from '@components/Umbler.vue'
    import Vue from 'vue'
    export default Vue.extend({
    components: {
      Maps,
      TracksFilter,
      Umbler,
    },
    name: 'App',
  })
</script>

<style>
</style>