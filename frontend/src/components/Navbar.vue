<template>
  <nav class="navbar navbar-expand-md navbar-success bg-success fixed-top">
    <div class="navbar-brand" id="navbar-title">Trekkpedia</div>
    <div class="float-right"><a href="https://www.strava.com/oauth/authorize?client_id=28106&redirect_uri=http://localhost:8000/strava-login&response_type=code&scope=activity:read_all">STRAVA</a></div>
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