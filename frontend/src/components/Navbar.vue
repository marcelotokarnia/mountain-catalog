<template>
  <nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
    <div class="navbar-brand" id="navbar-title">Trekkpedia</div>
  </nav>
</template>

<script lang="ts">
  import Vue from 'vue'
  export default Vue.extend({
    name: 'Navbar',
  })
</script>

<style scoped lang="css">
  #navbar-title {
    padding-left: 5rem;
  }
</style>