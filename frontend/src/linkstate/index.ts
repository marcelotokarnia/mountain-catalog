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
  hello: {
    __typename: 'Hello',
    msg: 'world',
  },
}

const resolvers: IResolverObject = {
  Mutation: {
    updateHello(_: any, { message }: any, { cache }: IContext): void {
      const data = {
        hello: {
          __typename: 'Hello',
          msg: message,
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
