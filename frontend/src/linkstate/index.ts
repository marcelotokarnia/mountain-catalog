import { IPosition } from '@typings/geo'
import { IMountain } from '@typings/mountains'
const mapQuery = require('@queries/mapState.graphql')
import { InMemoryCache } from 'apollo-cache-inmemory'

interface IResolverObject {
  Mutation?: IResolverProp
}

interface IResolverProp {
  [key: string]: (root: any, args: any, context: IContext) => void
}

interface IContext {
  cache: InMemoryCache
}

interface IDefaultProp {
  __typename: string
  [key: string]: any
}

interface IDefaultObject {
  [key: string]: IDefaultProp
}

const defaults: IDefaultObject = {
  smap: {
    __typename: 'SMap',
    center: {lat: -22, lng: -45, __typename: 'IPosition'} as IPosition,
    zoom: 5,
  },
  smePosition: {
    __typename: 'SMe',
    position: null,
  },
  smountainHint: {
    __typename: 'SMountainHint',
    mountain: null,
  },
  smountains: {
    __typename: 'SMountains',
    mountains: [] as IMountain[],
  },
}

const resolvers: IResolverObject = {
  Mutation: {
    updateMePosition(_: any, { position }: any, { cache }: IContext): any {
      const data = {
        smePosition: {
          __typename: 'SMe',
          position: {...position, __typename: 'IPosition'},
        },
      }
      cache.writeData({ data })
      return data
    },
    updateMountainHint(_: any, { mountain }: any, { cache }: IContext): any {
      const data = {
        smountainHint: {
          __typename: 'SMountains',
          mountain,
        },
      }
      cache.writeData({ data })
      return data
    },
    updateMountains(_: any, { mountains }: any, { cache }: IContext): any {
      const data = {
        smountains: {
          __typename: 'SMountains',
          mountains,
        },
      }
      cache.writeData({ data })
      return data
    },
    updateMap(_: any, { center, zoom }: any, { cache }: IContext): any {
      let mapState
      try {
        mapState = cache.readQuery<any>({
          query: mapQuery,
        }).map
      } catch (e) {
        mapState = null
      }

      const data = {
        smap: {
          __typename: 'SMap',
          center: {...center, __typename: 'IPosition'} || (mapState && mapState.center),
          zoom: zoom || (mapState && mapState.zoom),
        },
      }

      cache.writeData({ data })
      return data
    },
  },
}

export {
  resolvers,
  defaults,
}
