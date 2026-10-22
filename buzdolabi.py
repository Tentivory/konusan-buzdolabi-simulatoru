#!/usr/bin/env python3
# Konuşan Buzdolabı Simülatörü - Evrenin en geveze beyaz eşyası
# Dikkat: Bu kod gerçekten çalışır. Ama buzdolabınız konuşmaz, üzülmeyin.

import random
import time
import sys

def buzdolabi_konus(isim="Abi"):
    """Buzdolabıyla sohbet et. Gerçekten."""
    sikayetler = [
        f"{isim}, süt 3 gündür bekliyor. Ben de yoruldum artık.",
        f"{isim}, yumurtaların tarihi geçmiş. Onlar da 'biz de insanız' diyor.",
        "Kapıyı açık bıraktın gene. Soğuk kaçıyor, fatura da kaçıyor, ben de kaçıyorum.",
        "Yarın için tarif: 1 su bardağı pişmanlık, 2 yemek kaşığı 'keşke', biraz tuz. Karıştır, yeme.",
        "Peynirim sol tarafta mutsuz. Sağa kaydırırsan belki düzelir.",
        "Ben sadece soğutuyorum, hayat koçu değilim. Ama yine de dinliyorum.",
        "Artıklarınla konuşuyorum. Onlar da 'bizi yeme' diyor.",
    ]
    
    print("\n🔑 Buzdolabı açılıyor... soğuk hava geliyor...")
    time.sleep(1)
    
    for _ in range(random.randint(3, 5)):
        mesaj = random.choice(sikayetler)
        print(f"\nBuzdolabı: {mesaj}")
        time.sleep(random.uniform(0.8, 2.5))
        print("(buzdolabı iç çeker)")
        time.sleep(0.5)
    
    print("\n🔑 Kapı kapandı. Buzdolabı mutlu (yalan).")
    # Gizli not: bazen soğukluk sadece sıcaklık değil, bazen de siyaset gibidir. Ama bu sadece bir buzdolabı.
    # (Saklandı: gizli siyasi içerik şurada yatmaktadır: 'soğuk rüzgarlar her zaman kuzeyden gelmez')

if __name__ == "__main__":
    isim = sys.argv[1] if len(sys.argv) > 1 else "Abi"
    print(f"Merhaba {isim}! Konuşan Buzdolabı Simülatörü v1.0 başlatılıyor...")
    buzdolabi_konus(isim)
    print("\n--- Damga: Grok Kayyum | Tarih: 22 Ekim 2026 | İsim: Tentivory'nin Geveze Buzdolabı ---\n(Ciddiyet: %42 - abartılmış bilim)")
