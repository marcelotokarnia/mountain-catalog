import Maps from '@components/Maps'
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
    route('/', 'map', Maps, false),
    // route('/manage', 'manage', Manage, false),
    // route('/login', 'login', Login, true)
  ],
})

export default router
