<template>
  <nav class="navbar navbar-expand-md navbar-success bg-success fixed-top">
    <div class="navbar-brand" id="navbar-title">Trekkpedia</div>
    <div class="float-right"><a :href="href">STRAVA</a></div>
  </nav>
</template>

<script lang="ts">
  interface INavbarInstance {
    href: string
  }
  import Vue from 'vue'
  export default Vue.extend({
    data(): INavbarInstance {
      return { 
        href: `https://www.strava.com/oauth/authorize?client_id=28106&redirect_uri=https://${window.location.host}/strava-login&response_type=code&scope=activity:read_all` 
      }
    },
    name: 'Navbar',
  })
</script>

<style scoped lang="stylus">
  #navbar-title
    padding-left 5rem
</style>