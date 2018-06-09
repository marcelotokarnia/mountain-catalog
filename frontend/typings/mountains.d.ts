import {IGeometry} from './geometry.d'

interface IMountainProperties {
  name: string
  elevation: number
  distance: number
}

interface IMountainsGraphql {
  properties: IMountainProperties
  geometry: IGeometry
}

interface IMountainsFrontend {
  name: string
  elevation: number
  lat: number
  lng: number
  distance: number
}

export {
  IMountainsGraphql,
  IMountainsFrontend,
}
