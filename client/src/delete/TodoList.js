import React, { Component } from 'react';

import store from '@/store'
import * as actionTypes from '@/store/actionTypes'
import * as actionCreators from '@/store/actionCreators'
import TodoListUI from '@/components/TodoListUI'
import axios from 'axios'


class TodoList extends Component {
	constructor(props) {
		super(props);
		this.state = store.getState()
		this.changeInputValue = this.changeInputValue.bind(this)
		this.clickBtn = this.clickBtn.bind(this)
		this.deleteItem = this.deleteItem.bind(this)
		this.storeChange = this.storeChange.bind(this)    // 不订阅，this.state 中的取值会 get 不到 action 的变化
		store.subscribe(this.storeChange)   // 订阅 store 变化
	}

	componentDidMount() {
		const action = actionCreators.getTodoList()
		store.dispatch(action)
	}

	render() {
		return (
			<TodoListUI
				inputValue = {this.state.inputValue}
				changeInputValue = {this.changeInputValue}
				clickBtn = {this.clickBtn}
				list = {this.state.list}
				deleteItem = {this.deleteItem}
			/>
		)
	}

	changeInputValue(e){
		const action = actionCreators.changeInputAction(e.target.value)
		store.dispatch(action)
	}

	storeChange(){
		this.setState(store.getState());
	}

	clickBtn(){
		const action = actionCreators.addItemAction()
		store.dispatch(action)
	}

	deleteItem(index){
		const action = actionCreators.deleteItemAction(index)
		store.dispatch(action)
	}
}

export default TodoList;
