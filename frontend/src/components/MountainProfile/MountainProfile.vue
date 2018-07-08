<template>
  <div>
    {{$formatMessage({id: 'profile.profile.profile'})}}
    {{$route.params.id}}
  </div>
</template>

<script>
import Vue from 'vue'
export default Vue.extend({
  data() {

  },
  methods: {

  },
  name: 'MountainProfile',
  props: ['params'],
})
</script>