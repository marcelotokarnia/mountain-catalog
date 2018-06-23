declare let CSRFTOKEN: string

declare module '@locales/*.json' {
  const value: {
    [key: string]: string
  }
  export default value
}

declare module '*.vue' {
  import Vue from 'vue'
  export default Vue
}
