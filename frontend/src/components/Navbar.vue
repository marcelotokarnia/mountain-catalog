<template>
  <nav class="navbar navbar-expand-md navbar-success bg-success fixed-top">
    <router-link class="navbar-brand p-2" id="navbar-title" :to="'/'">Trekkpedia</router-link>
    <UserNavbar />
  </nav>
</template>

<script lang="ts">
  import Vue from 'vue'
  import UserNavbar from '@components/UserProfile/UserNavbar.vue'
  export default Vue.extend({
    components: {
      UserNavbar
    },
    name: 'Navbar',
  })
</script>

<style scoped lang="stylus">
  #navbar-title
    padding-left 5rem
  nav
    height 4rem
</style>