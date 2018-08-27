<template>
  <div>
    {{$formatMessage({id: 'profile.profile.profile'})}}
    {{user ? user.username : ''}}
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { ApolloQueryResult } from 'apollo-client'
const UserData = require('@queries/userData.graphql')
export default Vue.extend({
  apollo: {
    user: {
      query: UserData,
      result( result: ApolloQueryResult<{ user: { username: string} | null }>) {
        const { data: { user } } = result
        if (!user) {
          window.location.replace('/login')
        }
        this.user = user
      },
    },
  },
  data() : {user: {username: string} | null} {
    return {
      user: null
    }
  },
  methods: {

  },
  name: 'UserProfile',
  props: [],
})
</script>