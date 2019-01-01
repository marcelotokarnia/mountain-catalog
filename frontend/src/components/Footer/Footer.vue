<template>
  <nav class="navbar navbar-expand-md navbar-success bg-success fixed-bottom">
    <SocialMedia />
  </nav>
</template>

<script lang="ts">
    import SocialMedia from '@components/Footer/SocialMedia.vue'
    import Vue from 'vue'
    export default Vue.extend({
    components: {
      SocialMedia,
    },
    name: 'Footer',
  })
</script>

<style scoped lang="stylus">
  .navbar
    height 3rem
</style>