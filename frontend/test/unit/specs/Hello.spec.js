import {expect} from 'chai'
import Vue from 'vue'
import Hello from '@components/Hello'

describe('Hello.vue', () => {
  it('should render correct contents', () => {
    const Constructor = Vue.extend(Hello)
    const vm = new Constructor().$mount()
    expect(vm.$el.textContent)
      .equals('Hello John!')
    expect(vm.name).equal('John')
  })
})
