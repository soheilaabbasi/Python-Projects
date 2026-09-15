import streamlit as st
from tictactoe import TicTacToe


st.image('./images/tictactoe.png', width=600)
st.set_page_config(
    page_title="Tic Tac Toe",
    layout="centered",
)


def new_game():
    st.session_state.game = TicTacToe()
    st.session_state.game_over = False
    st.session_state.message = ""


# Create the game only once.
if "game" not in st.session_state:
    new_game()


game = st.session_state.game

st.title(":zap: Tic Tac Toe")
st.write(f"### Turn: **{game.player_turn}**")

# Show the board as a 3x3 grid.
for row in range(3):
    cols = st.columns(3)

    for col in range(3):
        cell = row * 3 + col + 1

        with cols[col]:
            # Disable a cell if it is already occupied or the game is over.
            disabled = game.board[cell] != " " or st.session_state.game_over

            if st.button(
                game.board[cell] if game.board[cell] != " " else str(cell),
                key=f"cell_{cell}",
                use_container_width=True,
                disabled=disabled,
            ):
                game.fix_spot(cell, game.player_turn)

                if game.has_player_won(game.player_turn):
                    st.session_state.game_over = True
                    st.session_state.message = (
                        f"🎉 Player **{game.player_turn}** won!"
                    )

                elif game.is_board_filled():
                    st.session_state.game_over = True
                    st.session_state.message = "🤝 It's a draw!"

                else:
                    game.swap_player_turn()

                st.rerun()


if st.session_state.message:
    st.success(st.session_state.message)

st.divider()

if st.button("🔄 New Game", use_container_width=True):
    new_game()
    st.rerun()
