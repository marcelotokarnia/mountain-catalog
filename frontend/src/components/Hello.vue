<template>
  <div>Hello {{name}}!</div>
</template>

<script lang="ts">
  import Vue from 'vue'
  interface IHello {
    name: string
  }
  export default Vue.extend({
    data(): IHello {
      return {
        name: 'John',
      }
    },
    name: 'Hello',
  })
</script>

<style>
</style>