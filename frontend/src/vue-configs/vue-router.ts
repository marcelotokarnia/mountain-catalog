import Maps from '@components/Maps'
import MountainProfile from '@components/MountainProfile'
import UserProfile from '@components/UserProfile'
import StravaLogin from '@components/login/StravaLogin'
import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

interface IRoute {
  component: typeof Vue
  meta: {
    isPublic: boolean,
  }
  name: string
  path: string
}

const route = (path: string, name: string, component: typeof Vue, isPublic: boolean): IRoute => ({
  component,
  meta: {isPublic},
  name,
  path,
})

const router = new VueRouter({
  mode: 'history',
  routes: [
    route('/strava-login', 'strava-login', StravaLogin, false),
    route('/profile', 'profile', UserProfile, false),
    route('/mountain/:id', 'mountain', MountainProfile, false),
    route('/', 'map', Maps, false),
    // route('/manage', 'manage', Manage, false),
    // route('/login', 'login', Login, true)
  ],
})

export default router
