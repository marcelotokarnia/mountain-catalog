import {Geometry} from './geometry.d'

interface MountainProperties {
  name: string
  elevation: number
}

interface MountainsGraphql {
  properties: MountainProperties
  geometry: Geometry
}

interface MountainsFrontend {
  name: string
  elevation: number
  lat: number
  lng: number
}

export {
  MountainsGraphql,
  MountainsFrontend
}