import pygame

# Inisialisasi pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Love Letter Animation")

# Warna
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Load gambar amplop
envelope_closed = pygame.image.load("images/amplop1.jpg")  # Gambar amplop tertutup
envelope_open = pygame.image.load("images/amplop2.jpg")  # Gambar amplop terbuka
envelope_open = pygame.transform.scale(envelope_open, (450, 400)) 

# Posisi amplop
envelope_x = (WIDTH - envelope_closed.get_width()) // 2
envelope_y = (HEIGHT - envelope_closed.get_height()) // 2

# Variabel untuk tracking status klik
is_open = False

# Font untuk teks
font = pygame.font.Font(None, 50)


running = True
while running:
    screen.fill(WHITE)  # Bersihkan layar
    if is_open:
        # Jika amplop terbuka, tampilkan amplop terbuka & teks
        screen.blit(envelope_open, (envelope_x, envelope_y))
        text = font.render("I Love You", True, RED)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, envelope_y + 150))
      

    else:
        # Jika belum diklik, tampilkan amplop tertutup
        screen.blit(envelope_closed, (envelope_x, envelope_y))

    pygame.display.flip()  # Update layar

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Cek jika klik terjadi di dalam area amplop
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if envelope_x <= mouse_x <= envelope_x + envelope_closed.get_width() and \
               envelope_y <= mouse_y <= envelope_y + envelope_closed.get_height():
                is_open = True  # Ubah status menjadi terbuka

pygame.quit()