import basicTable from '../../pages/table/basicTable';
import highTable from '../../pages/table/highTable';
import fetchTable from '../../pages/table/fetchTable';
import btnFetchTable from '../../pages/table/btnFetchTable';

export default [

	{
		path: '/table/basic',
		exact: true,
		component: basicTable
	}, {
		path : '/table/high',
		exact: true,
		component: highTable
	}, {
		path : '/table/pagination',
		exact: true,
		component: fetchTable
	}, {
		path : '/table/filter',
		exact: true,
		component: btnFetchTable
	}
]
