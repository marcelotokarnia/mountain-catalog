<template>
  <div>wait a little ... </div>
</template>

<script lang="ts">
  const getQueryVariable : (T: any) => string = variable => {
    const query = window.location.search.substring(1)
    const vars = query.split('&')
    for (let i = 0, e; i < vars.length; i++) {
      e = vars[i]
      const pair = e.split('=')
      if (decodeURIComponent(pair[0]) === variable) {
        return decodeURIComponent(pair[1])
      }
    }
    return ''
  }

  import Vue from 'vue'
  import axios from 'axios'
  export default Vue.extend({
    created() {
      if (window.location.search.indexOf('code') !== -1) {
        const code = getQueryVariable('code')
        const HOST = `${window.location.protocol}//${window.location.host}`
        axios.post(`${HOST}/authenticate`, {
          code
        }).then(() => {
          this.$router.push('/profile')
        })
      }
    },
    name: 'App',
  })
</script>