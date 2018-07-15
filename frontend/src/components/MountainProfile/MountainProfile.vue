<template>
  <div>
    {{loading ? 'loading': mountain.distance}}
  </div>
</template>

<script lang="ts">
interface IMountainProfile {
  loading: boolean
  mountain?: IMountain
  position?: IPosition
}

import { IPosition } from '@typings/geo'
import { IMountain } from '@typings/mountains'
import { ApolloQueryResult } from 'apollo-client'
import Vue from 'vue'
const mountainQuery = require('@queries/mountain.graphql')
const mePositionQuery = require('@queries/mePositionState.graphql')

export default Vue.extend({
  apollo: {
    mountain: {
      query: mountainQuery,
      watchLoading(isLoading) {
        this.loading = isLoading
      },
      skip() {
        return true
      },
    },
    smePosition: {
      query: mePositionQuery,
        result({data: {smePosition: { position: {lat, lng} } } }:
          ApolloQueryResult<{smePosition: { position: IPosition } }>) {
            this.position = {lat, lng}
            this.$apollo.queries.mountain.refetch({
              id: this.$route.params.id,
              position: this.position,
            })
            this.$apollo.queries.mountain.skip = false
        },
    },
  },
  data(): IMountainProfile {
    return {
      loading: true,
      mountain: undefined,
      position: undefined,
    }
  },
  methods: {

  },
  name: 'MountainProfile',
  props: ['params'],
})
</script>