<template>
  <div>
    <div>
      <Navbar />
      <Main>
        <router-view style="flex: 1;" />
        <TrekksFilter style="flex: 1;" />
      </Main>
    </div>

    <Umbler />
  </div>
</template>

<script lang="ts">
    import TrekksFilter from '@components/TrekksFilter'
    import Main from '@components/Main'
    import Navbar from '@components/Navbar'
    import Umbler from '@components/Umbler.vue'
    import Vue from 'vue'
    export default Vue.extend({
    components: {
      Main,
      Navbar,
      TrekksFilter,
      Umbler,
    },
    name: 'App',
  })
</script>

<style>
</style>