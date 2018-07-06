import { IPosition } from '@typings/geo'

interface IDataMountains {
  mountains: IMountain[]
}

interface IMountain {
  __typename?: string
  id: number
  name: string
  elevation: number
  country: string
  position: IPosition
  distance: number
  image: string
}

export {
  IMountain,
  IDataMountains,
}
