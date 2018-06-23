import Vue from 'vue'

declare module 'vue-intl' {
  export function install(Vue: any, options?: any): void
}

declare module 'vue/types/vue' {
  interface VueConstructor {  // tslint:disable-line interface-name
    setLocale: (locale: string) => void
    registerMessages: (locale: string, messages: any) => void
  }
}

// instance property
// declare module 'vue/types/vue' {
//   interface Vue {
//     $http: AxiosStatic;
//   }
// }

// constructor options
// import Vue from "vue";

// declare module "vue" {
//     export type ComponentOptions<T> = {
//         dependencies?: string | string[] | { [key: string]: string };
//     }
// }
