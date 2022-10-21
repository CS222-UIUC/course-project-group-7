import React from 'react'
import { render, screen } from '@testing-library/react'
import '@testing-library/jest-dom/extend-expect'
import Grid from './Grid'

describe('<Grid />', () => {
  test('it should mount', () => {
    render(<Grid />)

    const grid = screen.getByTestId('Grid')

    expect(grid).toBeInTheDocument()
  })
})
