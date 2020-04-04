const menuList = [
    {
        title:'首页',
        key:'/home',
    },
    {
        title: 'Fetch',
        key: '/fetch/demo'
    },
    {
        title:'UI',
        key:'/ui',
        children:[
            {
                title:'按钮',
                key:'/ui/buttons',
                children:[
                    {
                        title: '子按钮',
                        key: 'ul/buttons/bigButton'
                    }
                ]
            },
            {
                title:'弹框',
                key:'/ui/modals',
            },
            {
                title:'Loading',
                key:'/ui/loadings',
            },
            {
                title:'通知提醒',
                key:'/ui/notification',
            },
            {
                title:'全局Message',
                key:'/ui/messages',
            },
            {
                title:'Tab页签',
                key:'/ui/tabs',
            },
            {
                title:'图片画廊',
                key:'/ui/gallery',
            },
            {
                title:'轮播图',
                key:'/ui/carousel',
            }
        ]
    },
    {
        title:'表单',
        key:'/form',
        children:[
            {
                title: '基础表单',
                key: '/form/basic'
            },
            {
                title:'登录',
                key:'/form/login',
            },
            {
                title:'注册',
                key:'/form/reg',
            }
        ]
    },
    {
        title:'表格',
        key:'/table',
        children:[
            {
                title:'基础表格',
                key:'/table/basic',
            },
            {
                title:'高级表格',
                key:'/table/high',
            },
            {
                title:'表格分页(后端)',
                key:'/table/pagination',
            },
            {
                title:'表格过滤(后端,Btn)',
                key:'/table/filter',
            }
        ]
    },
    {
        title:'富文本',
        key:'/rich',
        disabled: true

    },
    {
        title:'城市管理',
        key:'/city'
    },
    {
        title:'订单管理',
        key:'/order',
        btnList:[
            {
                title:'订单详情',
                key:'/order/detail'
            },
            {
                title:'结束订单',
                key:'/order/finish'
            }
        ]
    },
    {
        title:'员工管理',
        key:'/user'
    },
    {
        title:'车辆地图',
        key:'/bikeMap'
    },
    {
        title:'图标',
        key:'/charts',
        children:[
            {
                title:'柱形图',
                key:'/charts/bar'
            },
            {
                title:'饼图',
                key:'/charts/pie'
            },
            {
                title:'折线图',
                key:'/charts/line'
            },
        ]
    },
    {
        title:'权限设置',
        key:'/permission'
    },
  ];
  export default menuList;
