import show from './show'
import fetch from './fetch'
import table from './table'
import form from './form'
import login from './login';

export const allDynamicRoutes = [

]

export const staticRoutes = [
	...show,
    ...fetch,
    ...table,
    ...form,
    ...login
]

export const routes = [
    ...show,
    ...fetch,
    ...table,
    ...form,
    ...login
];
