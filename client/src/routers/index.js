import {Article, Dashboard, Login, NotFound, Setting} from '@/pages'

const commonRoutes = [
	{
		pathname: '/login',
		component: Login
	}, {
		pathname: '/404',
		component: NotFound
	}
]

const privateRoutes = [
	{
		pathname: '/admin/dashboard',
		component: Dashboard
	}, {
		pathname: '/admin/article',
		component: Article
	}, {
		pathname: '/admin/setting',
		component: Setting
	}
]

export {
	commonRoutes,
	privateRoutes
}
