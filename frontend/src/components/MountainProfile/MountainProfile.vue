<template>
  <div>
    {{loading ? 'loading': mountain.name}}
  </div>
</template>

<script lang="ts">
interface IMountainProfile {
  loading: boolean
  mountain?: IMountain
}

import { IMountain } from '@typings/mountains'
import { ApolloQueryResult } from 'apollo-client'
import Vue from 'vue'
const mountainQuery = require('@queries/mountain.graphql')

export default Vue.extend({
  apollo: {
    mountain: {
      query: mountainQuery,
      variables() {
        return {
          id: this.$route.params.id,
        }
      },
      watchLoading(isLoading) {
        this.loading = isLoading
      },
    },
  },
  data(): IMountainProfile {
    return {
      loading: true,
      mountain: undefined,
    }
  },
  methods: {

  },
  name: 'MountainProfile',
  props: ['params'],
})
</script>