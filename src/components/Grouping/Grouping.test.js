import React from 'react'
import { render, screen } from '@testing-library/react'
import '@testing-library/jest-dom/extend-expect'
import Grouping from './Grouping'

describe('<Grouping />', () => {
  test('it should mount', () => {
    render(<Grouping />)

    const Grouping = screen.getByTestId('Grouping')

    expect(Grouping).toBeInTheDocument()
  })
})
