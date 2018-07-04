<template>
  <div>
    <Navbar />
    <Main>
      <router-view />
    </Main>
    <Footer />
  </div>
</template>

<script lang="ts">
    import Main from '@components/Main'
    import Navbar from '@components/Navbar'
    import Footer from '@components/Footer'
    import Vue from 'vue'
    export default Vue.extend({
    components: {
      Footer,
      Main,
      Navbar,
    },
    name: 'App',
  })
</script>