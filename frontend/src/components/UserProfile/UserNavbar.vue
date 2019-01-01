<template>
  <div class="ml-auto p-2 navbar-brand h-100">
    <div v-if="logged" class="h-100">
      <router-link :to="'/profile'" class="h-75">
        <img class="mh-100 w-auto round-img" :alt="`Profile of ${user.name}`" title="Strava" src="/static/icons/userplaceholder.png"/>
        <span>{{ user.name }}</span>
      </router-link>
    </div>
    <div v-if="!logged" class="h-100">
      Login with
      <a :href="href" class="h-75">
        <img class="mh-100 w-auto" alt="Login with Strava" title="Strava" src="/static/icons/social/strava.png"/>
      </a>
    </div>
  </div>
</template>

<script lang="ts">
  declare const user: any
  interface IUserNavbarInstance {
    href: string
    logged: boolean
    user: {
      name: string
      email: string
      username: string
    }
  }
  import Vue from 'vue'
  import { isEmpty } from 'ramda'
  export default Vue.extend({
    data(): IUserNavbarInstance {
      return { 
        href: `https://www.strava.com/oauth/authorize?client_id=28106&redirect_uri=https://${window.location.host}/strava-login&response_type=code&scope=activity:read_all`,
        logged: !isEmpty(user),
        user
      }
    },
    name: 'UserNavbar',
  })
</script>

<style scoped lang="stylus">
  .round-img
    border-radius 50%
</style>