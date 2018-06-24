import { IPosition } from '@typings/geo'

interface IDataMountains {
  mountains: IMountain[]
}

interface IMountain {
  id: number
  name: string
  elevation: number
  position: IPosition
  distance: number
  image: string
}

export {
  IMountain,
  IDataMountains,
}
