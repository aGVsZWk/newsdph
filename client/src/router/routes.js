import show from './show'
import fetch from './fetch'
import table from './table'
import form from './form'

export const allDynamicRoutes = [

]

export const staticRoutes = [
	...show,
    ...fetch,
    ...table,
    ...form
]

export const routes = [
    ...show,
    ...fetch,
    ...table,
    ...form
];
