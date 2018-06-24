import { IMountain } from '@typings/mountains'
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
  smountains: {
    __typename: 'SMountains',
    mountains: [] as IMountain[],
  },
}

const resolvers: IResolverObject = {
  Mutation: {
    updateMountains(_: any, { mountains }: any, { cache }: IContext): void {
      const data = {
        smountains: {
          __typename: 'SMountains',
          mountains,
        },
      }

      return cache.writeData({ data })
    },
  },
}

export {
  resolvers,
  defaults,
}
