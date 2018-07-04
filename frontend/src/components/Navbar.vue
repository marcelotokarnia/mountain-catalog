<template>
  <nav class="navbar navbar-expand-md navbar-success bg-success fixed-top">
    <div class="navbar-brand" id="navbar-title">Trekkpedia</div>
  </nav>
</template>

<script lang="ts">
  import Vue from 'vue'
  export default Vue.extend({
    name: 'Navbar',
  })
</script>

<style scoped lang="stylus">
  #navbar-title
    padding-left 5rem
</style>